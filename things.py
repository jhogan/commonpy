# vim: set et ts=4 sw=4 fdm=marker
"""
MIT License

Copyright (c) 2016 Jesse Hogan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from pdb import set_trace; B=set_trace

class things():
    def __init__(self):
        self.clear()

    def clear(self):
        self._ls=[]

    def __iter__(self):
        for t in self._list:
            yield t

    def append(self, t, uniq=False):
        if uniq:
            if t in self: return None
                    
        self._list.append(t)
        return t

    def __iadd__(self, t):
        if isinstance(t, thing):
            self.append(t)
        elif isinstance(t, things):
            ts = t
            for t in ts:
                self += t
        else: 
            raise ValueError('Unsupported object appended')
        return self

    def __iand__(self, t):
        self.append(t, uniq=True)
        return self

    def add(self, ts):
        self += ts
        return self

    def __add__(self, t):
        return self.add(t)

    @property
    def _list(self):
        if not hasattr(self, '_ls'):
            self._ls = []
        return self._ls

    @property
    def count(self):
        return len(self._list)

    def __len__(self):
        return self.count

    @property
    def isempty(self):
        return self.count == 0

    def __str__(self):
        if not self.isempty:
            r=''
            for i, t in enumerate(self):
                if i > 0: r += "\n"
                r += str(t)
            return r
        return ''

    def __setitem__(self, key, item):
        self._list[key]=item

    def __getitem__(self, key):
        if key.__class__ == int:
            return self._list[key]

        keyisobj = (type(key) != str and
                    type(key) != unicode)
        for e in self._list:
            if keyisobj:
                if e is key:
                    return e
            else:
                if e.str() == key:
                    return e
    @property
    def brokenrules(self):
        return rules()

    @property
    def isvalid(self):
        return self.brokenrules.isempty


class thing():
    def __init__(self):
        pass

    def add(self, t):
        th = things()
        th += self
        th += t
        return th

    def __add__(self, t):
        return self.add(t)



