import settings


def height_pro(procent):
    return settings.height / 100 * procent

def width_pro(procent):
    return settings.width / 100 * procent

def top_frame_height(procent):
    return settings.top_frame / 100 * procent


def bottom_frame_height(procent):
    return settings.bottom_frame / 100 * procent