from typing import TypeVar, Generic

UseCaseInput = TypeVar('UseCaseInput')
UseCaseOutput = TypeVar('UseCaseOutput')
RepositoryType = TypeVar('RepositoryType')


class UseCase(Generic[UseCaseInput, UseCaseOutput]):
    def __init__(self) -> None:
        pass

    async def execute(self, use_case_input: UseCaseInput) -> UseCaseOutput:
        return await self._execute(use_case_input)

    async def _execute(self, use_case_input: UseCaseInput) -> UseCaseOutput:
        raise NotImplementedError


class UseCaseRepositoryMixin(Generic[RepositoryType]):
    def __init__(self, repository: RepositoryType) -> None:
        self._repository = repository
