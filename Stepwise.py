import sublime
import sublime_plugin
import os
import shutil


class Stepper():

  tracked_ids = []

  def __init__(self, view):
    self.view = view

  def filename(self, count):
    filename, file_extension = os.path.splitext(self.view.file_name())
    return "{0}-step{1:02d}{2}".format(filename, count, file_extension)
  
  def next_filename(self):
    filename, file_extension = os.path.splitext(self.view.file_name())
    step_count = 1
    while os.path.isfile(self.filename(step_count)):
      step_count += 1
    return self.filename(step_count)

  def get_id(self):
    return self.view.buffer_id()

  def allow_tracking(self):
    the_id = self.get_id()
    if the_id not in self.tracked_ids:
      print "Adding {0} to tracked view ids".format(the_id)
      self.tracked_ids.append(the_id)
  
  def is_tracking(self):
    return self.get_id() in self.tracked_ids

  def is_saved(self):
    return self.view.file_name() is not None    

  def save_step(self):
      self.view.run_command('save')
      stepped_filename = self.next_filename()
      shutil.copy(self.view.file_name(), stepped_filename)
      print "Saved as {0}".format(stepped_filename)
      return stepped_filename
    
  def attempt_step(self):
    if self.is_tracking() and self.is_saved():
      return self.save_step()
    else:
      print "Did not save stepped version"
      return None

class StepwiseListener(sublime_plugin.EventListener):

  def on_post_save(self, view):
    if not hasattr(self, 'clicks'):
      self.clicks = []
      
    if id(view) in self.clicks:
      stepper = Stepper(view)
      filepath = stepper.attempt_step()  
      if filepath:
        filename = os.path.basename(filepath)
        sublime.message_dialog("{0} saved".format(filename))
    else:
      self.clicks.append(id(view))
      sublime.set_timeout(self.clear_clicks, 500)

  def clear_clicks(self):
    self.clicks = []

class StepwiseStepCommand(sublime_plugin.TextCommand):
      
  def run(self, edit):
    stepper = Stepper(self.view)
    # Automatically add to tracking list if you
    # consciously select to create a step
    stepper.allow_tracking()
    filepath = stepper.attempt_step()  
    if filepath:
      filename = os.path.basename(filepath)
      sublime.message_dialog("{0} saved".format(filename))

class StepwiseActivateCommand(sublime_plugin.TextCommand):
      
  def run(self, edit):
    stepper = Stepper(self.view)
    stepper.allow_tracking()
