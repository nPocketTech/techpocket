from techpocket.error import TechPocketApi
import base64


class Audio(TechPocketApi):
    def __init__(self, token):
        self._token = token

    def text_to_speech(self, save_path: str, text: str, return_type: str = 'mp3', speaker: str = 'female_normal',
                       mode: str = 'fast') -> None or str:
        '''
        [Parameters]
        ------------
        save_path: str,
            'return', 'path'
        text: str,
        return_type: str,
            'mp3', 'wav', 'mp3_in_zip', 'wav_in_zip', 'bytes'
        speaker: str,
            'female_normal'
        mode: str,
            'fast', 'natural'
        '''
        res = self._request('text_to_speech', self._token, text=text)

        if 'files' in res and 'base64' in res['files'][0]:
            decode_string = base64.b64decode(res['files'][0]['base64'])
            if save_path == 'return':
                return decode_string
            else:
                with open(save_path, 'wb') as f:
                    f.write(decode_string)

    def speech_enhancement(self, source_path: str, save_path: str, return_type: str = 'mp3', mode: str = 'standard',
                           level: str = 'high'):
        '''
        [Parameters]
        ------------
        source_path: str,
            file formate: '.wav'、 '.mp3'、 '.flac'、 '.ogg'
        save_path: str,
            'return', 'path'
        return_type: str,
            'mp3', 'mp3_in_zip', 'wav', 'wav_in_zip'
        mode: str,
            'standard', 'lite'
        level: str
            'high', 'medium', 'medium'
        '''
        pass

    def music_separation(self, source_path: str, save_folder: str, return_type: str, include: str):
        '''
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
        '''
        pass
