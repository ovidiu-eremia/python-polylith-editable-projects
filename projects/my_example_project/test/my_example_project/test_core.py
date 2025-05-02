from my_example_project.core import use_base


def test_sample():
    assert use_base().__name__.startswith("my_namespace")
