import os
import sublime, sublime_plugin

class LineFilterCommand(sublime_plugin.TextCommand):
    SEPARATOR = '\n'
    def run(self, edit, arg):
    	whole_view = sublime.Region(0, self.view.size())
    	content = self.view.substr(whole_view)
    	filtered_lines = filter(lambda item: arg in item, content.split('\n'))
    	self.view.replace(edit, whole_view, self.SEPARATOR.join(filtered_lines))    	

class LineFilterMainCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Enter pattern:", 'pattern', self.on_done, None, None)

    def on_done(self, text):
    	self.window.run_command("line_filter",{"arg": text})
