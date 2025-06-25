"""Core module for the Data Model."""

from typing import Any, ClassVar, cast

from pyspark.sql import types as t
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import registry as sa_registry
from sqlalchemy.schema import MetaData as SaMetaData
from sqlalchemy.schema import Table

from .my_comp import get_columns_ddls_from_table, get_struct_schema_from_table

DQ_DIALECT_METADATA_KEY = "dq_checks_target_dialect"


class Descriptor:
    print("@ Descriptor body")

    def __init__(self):
        print(f"@ Descriptor.__init__({self!r})")

    def __set_name__(self, owner, name):
        args = (self, owner, name)
        print(f"@ Descriptor.__set_name__{args!r}")

    def __set__(self, instance, value):
        args = (self, instance, value)
        print(f"@ Descriptor.__set__{args!r}")

    def __repr__(self):
        return "<Descriptor instance>"


class MetaData(SaMetaData):
    """MetaData for the Sql Alchemy Declarative Data Model.

    Args:
        SaMetaData (class): The SQLAlchemy MetaData super class.

    """

    def __init__(self, dialect: str | None = None, **kwargs: Any) -> None:  # noqa: ANN401
        """Init Method for the MetaData subclass."""
        super().__init__(**kwargs)
        self.info[DQ_DIALECT_METADATA_KEY] = dialect


class DataBase(DeclarativeBase):
    """Namespace for a group of tables that should belong to the same schema/db."""

    print("@ Builder body")
    __abstract__ = True
    __table_args__ = ({"extend_existing": True},)
    metadata: ClassVar[SaMetaData] = MetaData(info={DQ_DIALECT_METADATA_KEY: "mssql"})
    registry: ClassVar[sa_registry] = sa_registry()
    Base: ClassVar[Any]

    attr = Descriptor()

    def __init_subclass__(cls, *, run_init: bool = False) -> None:
        """Create in each subclass the variables needed to group tables in schema/db."""
        super().__init_subclass__()
        if DataBase in cls.__bases__:
            print(f"@ Builder.__init_subclass__({cls!r})")
            cls.__abstract__ = True
            cls.__table_args__ = ({"extend_existing": True},)
            cls.metadata = MetaData(info={DQ_DIALECT_METADATA_KEY: "mssql"})
            cls.registry = sa_registry(metadata=cls.metadata)

    @classmethod
    def get_struct_schema(cls) -> t.StructType:
        """Get the struct type schema from class table var.

        Returns:
            t.StructType: The struct type schema for this class.

        """
        table = cast("Table", cls.__table__)
        return get_struct_schema_from_table(table)

    @classmethod
    def get_string_schema(cls) -> str:
        """Get the string schema from this class table var.

        Returns:
            str: The comma and new line separated column sql strings.

        """
        table = cast("Table", cls.__table__)
        return ", ".join(get_columns_ddls_from_table(table))


class DataModel(MappedAsDataclass):
    """The base class for creating sqlachemy data models.

    Args:
        MappedAsDataclass (_type_): The base class that makes this a dataclass.
        DeclarativeBase (_type_): The base class that makes this an sqlalchemy model.

    """


print("importing my_ns.my_comp.core.py")

def some_func():
    pass
