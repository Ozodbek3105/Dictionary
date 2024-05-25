from PySide6.QtCore import QThread, Signal
import speech_recognition as sr


class SpeechRecognitionThread(QThread):
    finished = Signal(str)
    listening = Signal()
    recognizing = Signal()

    def __init__(self, parent=None):
        super(SpeechRecognitionThread, self).__init__(parent)
        self._running = True

    def stop(self):
        self._running = False

    def run(self):
        recognizer = sr.Recognizer()

        if self._running:
            with sr.Microphone() as source:
                print("Listening...")
                self.listening.emit()
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source)
                try:
                    print("Recognizing...")
                    self.recognizing.emit()
                    text = recognizer.recognize_google(audio)
                    self.finished.emit(text)
                except sr.UnknownValueError:
                    self.finished.emit("Could not understand the audio")
                except sr.RequestError as e:
                    self.finished.emit(f"Could not request results; {e}")
