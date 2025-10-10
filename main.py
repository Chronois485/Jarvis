from rich.console import Console
from rich.markdown import Markdown

import constants as const
from recognizer import Recognizer
from soundPlayer import SoundPlayer
from ttsEngine import TTSEngine
from commandManager import CommandManager

console: Console = Console()

print()
console.print(Markdown("# Starting"))

console.print("[dim]Initialization of main components[/dim]")
command_manager: CommandManager = CommandManager(const.COMMANDS)
recognizer_en: Recognizer = Recognizer(const.RecognitionModels.EN.value, language=const.Languages.ENGLISH.value)
recognizer_ua: Recognizer = Recognizer(const.RecognitionModels.UK.value, language=const.Languages.UKRAINIAN.value)
tts_engine: TTSEngine = TTSEngine(lang="uk")
sound_player: SoundPlayer = SoundPlayer()
running: bool = True
console.print("[dim green]Initialization completed[/dim green]")
console.print("[dim]Loading settings[/dim]")

console.print("[bold blue]Starting main loop[/bold blue]")

print()

console.print(Markdown("# Jarvis"))

while running:
    console.print("[italic blue]Waiting for hotword[/italic blue]")
    hotword_input: str = recognizer_en.recognize(recognizer_en.listen()).lower()

    if not "jarvis" in hotword_input: continue
    console.print("[bold green]Heard hotword[/bold green]")
    console.print("[italic blue]Waiting for command[/italic blue]")
    user_input: str = recognizer_ua.recognize(recognizer_ua.listen())
    console.print(f"[bold magenta]User: [/bold magenta] {user_input}")
    command = command_manager.determine_command(user_input)
    answer = command_manager.run_command(command)
    if not answer:
        continue
    if answer.lower() == const.ANSWER_EXIT.format(name=const.SETTINGS_MANAGER.get_settings("name")): running = False
    console.print(f"[bold blue]Jarvis: [/bold blue] {answer.capitalize()}")
    output_file: str = tts_engine.tts(answer.lower())
    sound_player.play_and_delete(output_file)
