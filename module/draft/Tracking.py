from deep_sort_realtime.deepsort_tracker import DeepSort


class Tracker:
  def __init__(self):
    self.object_tracker = DeepSort(
        max_age=30, # Maximum number of frames that an object will stay "alive" if we have lost it
        n_init=3,
        nms_max_overlap=0.5,
        max_cosine_distance=0.3,
        nn_budget=None,
        override_track_class=None,
        embedder="mobilenet",
        half=True,
        bgr=True,
        embedder_model_name=None,
        embedder_wts=None,
        polygon=False,
    )

  def track(self, detections, frame):
    tracks = self.object_tracker.update_tracks(detections, frame=frame)
    tracking_ids = []
    boxes = []
    for track in tracks:
      if not track.is_confirmed():
        continue
      tracking_ids.append(track.track_id)
      ltrb = track.to_ltrb()
      boxes.append(ltrb)
    return tracking_ids, boxes
