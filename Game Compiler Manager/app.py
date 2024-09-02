import os
import subprocess
import json
from datetime import datetime

class GameCompilerManager:
    def __init__(self, config_file='config.json'):
        self.config = self.load_config(config_file)
    
    def load_config(self, config_file):
        with open(config_file, 'r') as f:
            return json.load(f)

    def compile_game(self, game_name):
        if game_name not in self.config['games']:
            print(f"Error: No configuration found for game '{game_name}'")
            return
        
        game_config = self.config['games'][game_name]
        source_dir = game_config['source_dir']
        build_command = game_config['build_command']
        output_dir = game_config['output_dir']
        
        print(f"Compiling '{game_name}'...")
        self.run_build(source_dir, build_command, output_dir)
        
    def run_build(self, source_dir, build_command, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        log_file = os.path.join(output_dir, f"build_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        
        with open(log_file, 'w') as log:
            process = subprocess.Popen(build_command, shell=True, cwd=source_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            
            log.write(stdout.decode())
            log.write(stderr.decode())
        
        if process.returncode == 0:
            print(f"Build completed successfully. Logs saved to {log_file}")
        else:
            print(f"Build failed. Check the logs at {log_file}")

    def list_games(self):
        print("Available games for compilation:")
        for game_name in self.config['games']:
            print(f" - {game_name}")


    def main():
        manager = GameCompilerManager()
    
    while True:
        print("\n===== Game Compiler Manager =====")
        print("1. List Available Games")
        print("2. Compile a Game")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.list_games()
        elif choice == '2':
            game_name = input("Enter the game name: ")
            manager.compile_game(game_name)
        elif choice == '3':
            print("Exiting Game Compiler Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        if __name__ == "__main__":
            main()
