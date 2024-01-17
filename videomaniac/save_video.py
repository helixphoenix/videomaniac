from videomaniac.data import CapturedVideo
from videomaniac.public.models import Video


def save_video(video: CapturedVideo):
    saved_video= Video(name=video.name,width=CapturedVideo.width,
                       height=video.height,
                       resolution=video.resolution,
                       frame_rate=video.frame_rate,
                       number_of_frames=video.number_of_frames
                       )
    saved_video.save()
    return saved_video