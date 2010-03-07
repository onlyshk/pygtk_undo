#!/usr/bin/env python
# -*- coding:utf-8 -*-

import gtk

class UndoableBuffer(gtk.TextBuffer):
    
    def __init__(self):
        gtk.TextBuffer.__init__(self)
        self.undo_stack = []
        self.redo_stack = []
        self.connect('insert-text', self.on_insert_text)
        self.connect('delete-range', self.on_delete_range)

    def on_insert_text(self, textbuffer, text_iter, text, length):
         pass
        
    def on_delete_range(self, text_buffer, start_iter, end_iter):
         pass

    def begin_not_undoable_action(self):
         pass        
    
    def undo(self):
         pass

    def redo(self):
         pass
