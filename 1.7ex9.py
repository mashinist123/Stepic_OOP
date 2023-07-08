class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        return Video.play(cls.videos[video_indx])


v1 = Video()
v1.create('Python')
YouTube.add_video(v1)
YouTube.play(0)
v2 = Video()
v2.create('Python ООП')
YouTube.add_video(v2)
YouTube.play(1)