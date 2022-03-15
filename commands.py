from competitive_history_command import CompetitiveHistoryCommand
from competitive_status_command import CompetitiveStatusCommand
from help_command import HelpCommand

commands = [
    CompetitiveStatusCommand(),
    CompetitiveHistoryCommand(),
    HelpCommand()
]
