from browser.browser import CHROME


class Executor:

    def __init__(self, execute_data):
        self._execute_data = execute_data

    async def run(self):
        execute_func = self._execute_data['func']
        execute_params = self._execute_data['params']
        await CHROME.execute(execute_func, execute_params)
