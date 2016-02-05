# -*- coding: utf-8 -*-
"""
tabulator
---------

Classes for creating tabs.
"""
from folium.element import Element, MacroElement, Html, Template

class Tabulator(MacroElement):
    def __init__(self):
        super(Tabulator, self).__init__()
        self._name = 'Tabulator'

        self._template = Template(u"""
        {% macro header(this, kwargs) %}
            <style>
                body {height: initial;}

                {{this.get_name()}} * {
                    box-sizing: initial;
                    -webkit-box-sizing: initial;
                }
                {{this.get_name()}} ul {
                    list-style: none;
                    padding: 0 0 0 10px;
                    min-width: 460px;
                }

                {{this.get_name()}} li {
                    float: left;
                    position: relative;
                    height: 30px;
                    border-radius: 5px 10px 0 0;
                    margin-left: -10px;
                    text-shadow: 1px 1px 0 #bbb;
                    box-shadow: 0px 0px 10px rgba(0,0,0,.5);
                    transition: .2s;
                }

                {{this.get_name()}} a {
                    display: block;
                    position: relative;
                    width: 90px;
                    height: 20px;
                    padding: 6px 10px 20px 0;
                    border-radius: 5px 10px 0 0;
                    background: #eee;
                    color: #ddd;
                    text-align: center;
                    text-decoration: none;
                    transition: .2s;
                }

                {{this.get_name()}} li:hover {
                    z-index: 1;
                }

                {{this.get_name()}} li:hover a {
                    background: #ccc;
                    color: #000;
                }

                {{this.get_name()}} .selected {
                    z-index: 2;
                }

                {{this.get_name()}} .selected:hover a {
                    background: #fff;
                    color: #000;
                }
                {{this.get_name()}} .selected a {
                    z-index: 3;
                    background: #fff;
                    color: #000;
                    text-shadow: none;
                    font-weight: 500;
                }

                {{this.get_name()}} .{{this.get_name()}}_tabs {
                    position: relative;
                    z-index: 1;
                    clear: both;
                    min-width: 420px;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0,0,0,.5);
                    background: #fff;
                    display: none;
                }
            </style>
        {% endmacro %}
        {% macro html(this, kwargs) %}
            <{{this.get_name()}}>
                <ul>
                    {% for key, tab in this._children.items() %}
                    <li><a href="#" class="{{this.get_name()}}_tablk" id="{{tab.get_name()}}">{{tab.title}}</a></li>
                    {% endfor %}
                </ul>
                {% for key, tab in this._children.items() %}
                    <section class="{{this.get_name()}}_tabs" id="{{tab.get_name()}}_" style="display:none;">
                        {{tab.render()}}
                    </section>
                {% endfor %}
            </{{this.get_name()}}>
        {% endmacro %}

        {% macro script(this, kwargs) %}
            $($('.{{this.get_name()}}_tablk')[0].parentElement).addClass('selected');
            $($('.{{this.get_name()}}_tabs')[0]).css('display','block');
            $('.{{this.get_name()}}_tablk').click(function(e) {
                $(e.target.parentElement.parentElement.parentElement)
                    .children('.{{this.get_name()}}_tabs')
                    .css('display','none');
                $('#'+e.target.id+'_').css('display','block');
                $(e.target.parentElement.parentElement).children().removeClass('selected')
                $(e.target.parentElement).addClass('selected')
                });
        {% endmacro %}
        """)  # noqa


class Tab(Element):
    def __init__(self, title):
        super(Tab,self).__init__()
        self._name = 'Tab'
        self.title = title

        self._template = Template(u"""
        This is {{this.title}}.
        """)  # noqa

        
class Html(Element):
    """Create an HTML div object for embedding data.

    Parameters
    ----------
    data : str
        The HTML data to be embedded.
    width : int or str, default '100%'
        The width of the output div element.
        Ex: 120 , '120px', '80%'
    height : int or str, default '100%'
        The height of the output div element.
        Ex: 120 , '120px', '80%'
    """

    def __init__(self, data, width="100%", height="100%"):
        super(Html, self).__init__()
        self._name = 'Html'
        self.data = data

        self.width = _parse_size(width)
        self.height = _parse_size(height)

        self._template = Template(u"""
        <div id="{{this.get_name()}}"
                style="width: {{this.width[0]}}{{this.width[1]}}; height: {{this.height[0]}}{{this.height[1]}};">
                {{this.data|e}}</div>
                """)  # noqa
