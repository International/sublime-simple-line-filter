Get the whole contents of the view buffer in sublime:

```python
import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
	    content = self.view.substr(sublime.Region(0, self.view.size()))
	    print("whole contents:", content)
```	    

Replace the contents of the view:

```python
import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		whole_view = sublime.Region(0, self.view.size())
		self.view.replace(edit, whole_view, "Potato")
```

Input dialog ( opens in bottom ):
```python
import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel("Say something:", 'something', self.on_done, None, None)

    def on_done(self, text):
    	print("text is", text)
```

