from yt_dlp.extractor.youtube import YoutubeIE


class Youtube_CustomChaptersIE(YoutubeIE, plugin_name='CustomChapters'):
    def _extract_chapters_from_description(self, description, duration):
        filepath = self._configuration_arg('chapters_file', [None], ie_key='Youtube', casesense=True)[0]
        if filepath:
            with open(filepath, encoding='utf-8') as f:
                description = f.read()
        return super()._extract_chapters_from_description(description, duration)


__all__ = []
