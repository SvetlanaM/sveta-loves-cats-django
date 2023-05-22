from typing import TYPE_CHECKING, Type, TypeVar

T = TypeVar("T")


def with_typehint(baseclass: Type[T]) -> Type[T]:
    """
    Useful function to make mixins with baseclass typehint

    ```
    class ReadonlyMixin(with_typehint(BaseAdmin))):
        ...
    ```
    """
    if TYPE_CHECKING:
        return baseclass
    return object
