import base64
import pathlib
from pathlib import Path
from scipy.io import wavfile


class Audio:
    def __init__(self, _request):
        self._request = _request

    def text_to_speech(self, text: str, save_folder='', return_type: str = 'mp3',
                       speaker: str = 'female_normal', mode: str = 'fast') -> dict:
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
        save_path = self._handle_path(save_folder)
        files = self._request('text_to_speech', text=text, mode=mode, return_type=return_type)

        for d in files['files']:
            data_bytes = base64.b64decode(d['base64'])
            if save_path:
                Path(save_path / d['name']).write_bytes(data_bytes)

        return files['files']

    def speech_enhancement(self, source_path: str, save_folder: str, return_type: str = 'mp3', mode: str = 'standard',
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
        save_path = self._handle_path(save_folder)
        files = self._request('speech_enhancement', audio=open(source_path, 'rb'), mode=mode, return_type=return_type,
                              level=level)

        for d in files['files']:
            data_bytes = base64.b64decode(d['base64'])
            if save_path:
                Path(save_path / d['name']).write_bytes(data_bytes)

        return files['files']

    def music_separation(self, source_path: str = '', save_folder: str = '', return_type: str = 'mp3_in_zip',
                         include: str = 'both'):
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
        include: str
            'both', 'vocal', 'music'
        '''
        save_path = self._handle_path(save_folder)
        files = self._request('speech_enhancement', audio=open(source_path, 'rb'), return_type=return_type,
                              include=include)

        for d in files['files']:
            data_bytes = base64.b64decode(d['base64'])
            if save_path:
                Path(save_path / d['name']).write_bytes(data_bytes)

        return files['files']

    @staticmethod
    def _handle_path(save_to: str) -> pathlib.Path:
        path_obj = Path(save_to)

        # 如果不存在則創建父資料夾路徑
        if path_obj != '':
            if path_obj.suffix:
                path_obj.parent.mkdir(parents=True, exist_ok=True)
                open(path_obj, 'w').close()
            else:
                path_obj.mkdir(parents=True, exist_ok=True)

        return path_obj
