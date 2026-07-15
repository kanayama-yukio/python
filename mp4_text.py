import moviepy as mp
import speech_recognition as sr

# Mp4_to_Text(video_path)
def Mp4_to_Text(video_path):
    
    audio_file = "temp_audio.wav" # 抽出した音声ファイル
    output_file = "outtext.txt"

    # 動画から音声を抽出
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_file)

    # 音声からテキストを抽出
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="ja") # 日本語指定
    print("文字起こし結果:")
    print(text)

    # テキストを保存
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

# mp4_to_text(video_path)
def mp4_to_text(video_path):
    
    audio_file = "temp_audio.wav" # 抽出した音声ファイル
    output_file = "outtext.txt"

    # 動画から音声を抽出
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_file)

    # 音声からテキストを抽出
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="ja") # 日本語指定

    # テキストを保存
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

    return text


if __name__ == "__main__":

    # 動画ファイルのパス
    video_path = "Video.mp4"
    #text = Mp4_to_Text(video_path)
    text = mp4_to_text(video_path)
    print(text)
