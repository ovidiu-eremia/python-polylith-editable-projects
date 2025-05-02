from my_example_project.core import use_base #, use_my_other_project


def test_should_use_base():
    assert use_base().__name__.startswith("my_namespace")


# def test_should_use_my_other_project():
#     assert use_my_other_project().__name__.startswith("my_other_project")
