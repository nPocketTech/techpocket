from techpocket.techpocket_api.techpocket_api import TechPocketApi


class VoiceProcessing(TechPocketApi):
    def __init__(self):
        super(VoiceProcessing, self).__init__()

    def text_to_speech(self, save_path: str, text: str, return_type: str, speaker: str, mode: str) -> None:
        """
        [Parameters]
        ------------
        save_path: str,
        text: str,
        return_type: str,
            'mp3', 'wav', 'mp3_in_zip', 'wav_in_zip', 'bytes'
        speaker: str,
            'female_normal'
        mode: str,
            'fast', 'natural'
        """
        pass

    def speech_enhancement(self, source_path: str, save_path: str, return_type: str, mode: str, level: str):
        """
        [Parameters]
        ------------
        source_path: str,
            file formate: '.wav'、 '.mp3'、 '.flac'、 '.ogg'
        save_path: str,
        return_type: str,
            'mp3', 'mp3_in_zip', 'wav', 'wav_in_zip'
        mode: str,
            'standard', 'lite'
        level: str
            'high', 'medium', 'medium'
        """
        pass

    def music_separation(self, source_path: str, save_folder: str, return_type: str, include: str):
        """
        [Parameters]
        ------------
        source_path: str,
            file formate: '.wav'、 '.mp3'、 '.flac'、 '.ogg'
        save_path: str,
        return_type: str,
            'mp3', 'mp3_in_zip', 'wav', 'wav_in_zip'
        mode: str,
            'standard', 'lite'
        level: str
            'both', 'vocal', 'music'
        """
        pass