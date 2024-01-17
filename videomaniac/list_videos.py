from videomaniac.public.models import Video

def list_all():
    return Video.query.all()
             
    
