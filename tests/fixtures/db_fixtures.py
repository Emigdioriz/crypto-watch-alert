# from contextlib import contextmanager
# from datetime import datetime
# import pytest
# from sqlalchemy.pool import NullPool
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy import event
# from infraestructure.config.db import mapper_registry
# from infraestructure.config.env import TestSettings


import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from src.infraestructure.config.db import mapper_registry, get_session
from fastapi.testclient import TestClient
from src.main import app



# @pytest.fixture(scope="session")
# async def engine():
#     engine = create_async_engine(str(TestSettings().database_url), poolclass=NullPool)
#     yield engine


# @pytest.fixture
# async def session(engine):
#     async with engine.begin() as conn:
#         await conn.run_sync(mapper_registry.metadata.create_all)
    
#     async with AsyncSession(engine, expire_on_commit=False) as session:
#         yield session
    
#     async with engine.begin() as conn:
#         await conn.run_sync(mapper_registry.metadata.drop_all)


# @contextmanager
# def _mock_db_time(*, model, time=datetime(2024, 1, 1)):
#     def fake_time_handler(mapper, connection, target):
#         if hasattr(target, 'created_at'):
#             target.created_at = time
#         if hasattr(target, 'updated_at'):
#             target.updated_at = time

#     event.listen(model, 'before_insert', fake_time_handler)

#     yield time

#     event.remove(model, 'before_insert', fake_time_handler)


# @pytest.fixture
# def mock_db_time():
#     return _mock_db_time

@pytest.fixture
async def db_session():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(mapper_registry.metadata.create_all)
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
    await engine.dispose()


@pytest.fixture
def client():
    # Cria engine e sessão síncrona em memória para usar com TestClient
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, scoped_session
    from sqlalchemy.pool import StaticPool
    
    # Usa StaticPool e check_same_thread=False para permitir uso em diferentes threads
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=True
    )
    
    # Cria as tabelas
    mapper_registry.metadata.create_all(engine)
    
    # Usa scoped_session para thread-safety
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    
    def get_test_session():
        session = Session()
        try:
            yield session
        finally:
            session.close()
            Session.remove()
    
    app.dependency_overrides[get_session] = get_test_session
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides = {}
    Session.remove()
    engine.dispose() 