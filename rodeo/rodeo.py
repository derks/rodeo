
import re
import pystache
from StringIO import StringIO
from blessings import Terminal

term = Terminal()

def _termify(func, txt, raise_error=False):
    """
    Call the Terminal() `func` passing it `txt`.  Raise an error only if
    raise_error is True, otherwise just return `txt`.
    """
    funcs = func.split(',')
    try:
        for func in funcs:
            txt = getattr(term, func)(txt)
        return txt
    except TypeError as e:
        if raise_error is True:
            raise
        else:
            return txt
        
def _bless(txt, strict=False):
    """
    Parse the `txt` for specific markup to pass to the Blessings Terminal()
    module.  Raise errors only if `strict==True`.
    """
    
    ### YES, I KNOW... THIS FUNCTION IS FUCKING UGLY.  ITS A QUICK HACK,
    ### AND I WILL REWRITE IT SOON.
    
    res_parts = []
    for line in StringIO(txt).readlines():
        parts = line.split(' ')
        
        inside_block = False
        block_txt = None
        func = None
        for part in parts:
            ### We don't use if/elif here because we only want to do the 
            ### regular expression matching if necessary.
            
            # there are no spaces within the block
            full_block = re.match('(.*)(\[r:(.*)\])(.*)(\[\/r\])(.*)', part)
            if full_block:
                func = full_block.group(3)
                block_txt = _termify(func, full_block.group(4), strict)
                full_txt = "%s%s%s" % (
                    full_block.group(1),
                    block_txt,
                    full_block.group(6), 
                    )
                    
                res_parts.append(full_txt.strip('\n') + ' ')
                inside_block = False
                func = None
                block_txt = None
                continue
                
            # blocks with spaces break up the parts
            start_block = re.match('(.*)(\[r:(.*)\])(.*)', part)
            if start_block:
                inside_block = True
                start_txt = start_block.group(1)
                block_txt = start_block.group(4)
                func = start_block.group(3)
                continue
            
            end_block = re.match('(.*)(\[\/r\])(.*)', part)
            if end_block:
                block_txt = block_txt + ' ' + end_block.group(1)
                end_txt = "%s%s" % (
                    _termify(func, block_txt, strict),
                    end_block.group(3),
                    )
                
                res_parts.append(start_txt + end_txt.strip('\n') + ' ')     
                start_txt = None 
                block_txt = None
                inside_block = False
                func = None
                continue
            
            # if the first two don't continue, then...
            if inside_block:
                if len(part) > 0:
                    block_txt = block_txt + ' ' + part
                continue
                
            # otherwise
            res_parts.append(part.strip('\n') + ' ')

        # re-add the newline, since we are looping over .readlines()
        res_parts.append('\n')
        
    res_txt = ''.join(res_parts)
    return res_txt
    
def render(template_data, context=None, strict=False, **kw):
    """
    Render a rodeo template (data).
    
    :param template: The template path to render.
    :param context: The context dictionary to pass to the template.
    :param strict: Whether or not to raise errors during parsing.
    :param kw: Additional keyword arguments to pass to PyStache.
    :returns: string
    
    """
    txt = pystache.render(template_data, context, **kw)
    txt = _bless(txt, strict)
    return txt

def render_file(template_path, context=None, strict=False, **kw):
    """
    Same as `render`, but takes a file path, reads it, and then passes that
    data to render().
    """
    data = open(template_path, 'r').read()
    return render(data, context, strict, **kw)
