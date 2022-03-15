from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):

    @abstractmethod
    def command_name(self):
        pass

    @abstractmethod
    async def execute(self, **kwargs):
        pass
