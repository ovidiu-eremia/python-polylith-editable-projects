"""Module with ddl utility functions."""

from typing import cast

from databricks.sqlalchemy.base import DatabricksDialect
from pyspark.sql import types as t
from sqlalchemy.schema import Table


def get_struct_schema_from_table(table: Table) -> t.StructType:
    """Get the StructType schema from a SqlAlchemy table.

    Args:
        table (Table): The SqlAlchemy table to get the schema for.

    Returns:
        t.DataType: The Pyspark data type as it can be a single column.

    """
    columns_ddls = get_columns_ddls_from_table(table)
    data_type = t._parse_datatype_string(", ".join(columns_ddls))  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    return cast("t.StructType", data_type)


def get_columns_ddls_from_table(table: Table) -> list[str]:
    """Get the columns ddl strings from a SqlAlchemy table.

    Args:
        table (Table): The SqlAlchemy table

    Returns:
        list[str]: The list of columns str ddls for the table.

    """
    dialect = DatabricksDialect()
    ddl_compiler = dialect.ddl_compiler(dialect, None)
    return [ddl_compiler.get_column_specification(col) for col in table.columns]


def my_comp_func():
    return None
