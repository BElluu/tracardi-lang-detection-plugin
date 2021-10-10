import asyncio
from tracardi_plugin_sdk.service.plugin_runner import run_plugin
from tracardi_lang_detection.plugin import LangDetectAction

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


init = {}
payload = {
    'key': '1234',
    'txt': 'Hola!'
}

result = run_plugin(LangDetectAction, init, payload)

print("OUTPUT:", result.output)
