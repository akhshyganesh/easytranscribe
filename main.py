#!/usr/bin/env python3
"""
Example usage script for easytranscribe library.
This demonstrates how to use the library for live transcription.
"""

from easytranscribe import capture_and_transcribe


def main():
    """Main function to demonstrate live transcription."""
    try:
        print("🎤 Starting live transcription...")
        text = capture_and_transcribe(model_name="base")
        print(f"📝 Transcribed: {text}")
        # Here you can send 'text' to other services for further processing
    except KeyboardInterrupt:
        print("\n👋 Transcription stopped by user.")
    except Exception as e:
        print(f"❌ Error during transcription: {e}")


if __name__ == "__main__":
    print("🚀 EasyTranscribe Demo")
    print("Press Ctrl+C to stop at any time")
    
    while True:
        try:
            main()
            print("\n" + "="*50)
            input("Press Enter to transcribe again or Ctrl+C to exit...")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
