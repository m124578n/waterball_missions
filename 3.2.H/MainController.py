from Key import Key
from Marco import Marco


class MainController:
    def __init__(self, command: dict):
        self.history_undo: list = []
        self.history: list = []
        self.keys: list[Key] = []
        key = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        for k in key:
            self.keys.append(Key(k))
        self.command: dict = command

    def start(self):
        while True:
            for k in self.keys:
                if k.key:
                    print(f"{k.name} {k}")
            choose = input("（１）設置快捷鍵（２）undo（３）redo（字母）快捷鍵   請選擇：")
            if choose == '1':
                self.set_key()
            elif choose == '2':
                self.undo()
            elif choose == '3':
                self.redo()
            else:
                for k in self.keys:
                    if k.name == choose:
                        k.execute()
                        self.history.append(k)
                        self.history_undo = []

    def set_key(self):
        use_marco = input("請問要使用巨集嗎 y/n：")
        key = input("請選擇要設定的快捷鍵（字母）：")
        print(f"請選擇要設定在 {key} 上的指令：")
        for i, x in self.command.items():
            print(f"（{i}）{x}")
        command = input()
        for k in self.keys:
            if k.name == key:
                if use_marco == 'y':
                    marco = Marco()
                    commands = command.split(" ")
                    for c in commands:
                        marco.command.append(self.command[c])
                    k.key = marco
                    self.command[key] = marco
                else:
                    k.key = self.command[command]

    def reset(self):
        self.keys: list[Key] = []
        key = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        for k in key:
            self.keys.append(Key(k))

    def undo(self):
        if not self.history:
            print("目前為最舊指令")
            return
        key = self.history.pop(-1)
        key.undo()
        self.history_undo.append(key)

    def redo(self):
        if not self.history_undo:
            print("目前為最新指令")
            return
        key = self.history_undo.pop(-1)
        key.execute()
        self.history.append(key)
