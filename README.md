Rodeo Templates
===============

Rodeo Templates are a mashup of Mustache Templates, with markup using the 
Blessings module.  This project is a proof of concept, and the code is less
than stellar.  I will revamp everything if people actually use this.

 * pyStache: https://github.com/defunkt/pystache
 * Blessings: https://github.com/erikrose/blessings

The official source is here:

 * http://github.com/derks/rodeo
    
Examples:

Here is an example templates:

<pre>
This is a [r:red]Rodeo Template[/r] example.  It is a [r:green]mashup[/r] of
[r:cyan]pyStache[/r] and [r:cyan]Blessings[/r].

The markup is loosely coupled to Blessings.  You can do things like:

    * Make [r:blue]text[/r] [r:green]more[/r] [r:yellow]colorful[/r]
    * [r:underline]Underline[/r] and [r:bold]Bold[/r]
    * You can [r:reverse]reverse[/r] the background/foreground
    * Add [r:italic]italics[/r]
    * Or make text [r:standout]standout[/r]
    * You can even [r:bold,red,underline]combine multiple features[/r]
    * [r:shadow]Etc...[/r]

You can iterate over data:

{{#people}}
    * Hello [r:green]{{first_name}} {{last_name}}[/r].
{{/people}}
</pre>


And the code to render it:

```python
import rodeo

data = dict()
data['people'] = [
    dict(first_name='John', last_name='Doe'),
    dict(first_name='Rita', last_name='Sampson'),
    ]
print rodeo.render_file('examples/test.rodeo', data)
```

This actually renders the template to:

<pre>
    u' \nThis is a \x1b[31mRodeo Template\x1b(B\x1b[m example.  It is a \x1b[32mmashup\x1b(B\x1b[m of \n\x1b[36mpyStache\x1b(B\x1b[m and \x1b[36mBlessings\x1b(B\x1b[m. \n \nThe markup is loosely coupled to Blessings.  You can do things like: \n \n    * Make \x1b[34mtext\x1b(B\x1b[m \x1b[32mmore\x1b(B\x1b[m \x1b[33mcolorful\x1b(B\x1b[m \n    * \x1b[4mUnderline\x1b(B\x1b[m and \x1b[1mBold\x1b(B\x1b[m \n    * You can \x1b[7mreverse\x1b(B\x1b[m the background/foreground \n    * Add italics\x1b(B\x1b[m \n    * Or make text \x1b[7mstandout\x1b(B\x1b[m \n    * You can even \x1b[4m\x1b[31m\x1b[1mcombine multiple features\x1b(B\x1b[m\x1b(B\x1b[m\x1b(B\x1b[m \n    * Etc...\x1b(B\x1b[m \n \nYou can iterate over data: \n \n    * Hello \x1b[32mJohn Doe\x1b(B\x1b[m. \n    * Hello \x1b[32mRita Sampson\x1b(B\x1b[m. \n'
</pre>