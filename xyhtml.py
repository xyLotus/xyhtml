""" HTMLLIB is a libary for writing HTML Code in Python,
you could say it's some kind of Framework. """

# Credits
__author__ = 'Lotus'
__version__ = 0.5


# File to be read to get skeleton
parse_file = r'C:\Users\Martin\Desktop\EVERYTHING\Python\HTMLLIB\skeleton.txt'

def get_skeleton() -> str:
    """ Function that reads HTML skeleton from default
    set path file. """
    # Trying to read skeleton src file
    try:
        with open(parse_file, 'r') as f:
            # Getting Skeleton Source
            skeleton: str = f.read()
    except FileNotFoundError as e:
        print(f'An error occurred while trying to skeleton src file: {e}')
        exit() # Exiting program if mandatory file is missing

    return skeleton


class Tags:
    """ This is the class that contains all the HTML5 Tags. This is used
    instead of just typing the tag name in the function, as this also holds
    if a certain tag needs a closing tag. An underscore has been added to 
    all tags which are also keywords Python. """

    a           = 'a'
    abbr        = 'abbr'
    address     = 'address'
    area        = 'area'
    article     = 'article'
    aside       = 'aside'
    audio       = 'audio'
    b           = 'b'
    base        = 'base'
    bdi         = 'bdi'
    bdo         = 'bdo'
    blockquote  = 'blockquote'
    body        = 'body'
    br          = 'br'
    button      = 'button'
    canvas      = 'canvas'
    caption     = 'caption'
    cite        = 'cite'
    code        = 'code'
    col         = 'col'
    colgroup    = 'colgroup'
    data        = 'data'
    datalist    = 'datalist'
    dd          = 'dd'
    del_        = 'del'
    details     = 'details'
    dfn         = 'dfn'
    dialog      = 'dialog'
    div			= 'div'
    dl			= 'dl'
    dt			= 'dt'
    em			= 'em'
    embed		= 'embed'
    fieldset	= 'fieldset'
    figcaption	= 'figcaption'
    figure		= 'figure'
    footer		= 'footer'
    form		= 'form'
    efine		= 'efine'
    h1			= 'h1'
    h2			= 'h2'
    h3			= 'h3'
    h4			= 'h4'
    h5			= 'h5'
    h6			= 'h6'
    head		= 'head'
    header		= 'header'
    hr			= 'hr'
    html		= 'html'
    i			= 'i'
    iframe		= 'iframe'
    img			= 'img'
    input		= 'input'
    ins			= 'ins'
    kbd			= 'kbd'
    label		= 'label'
    legend		= 'legend'
    li			= 'li'
    link		= 'link'
    main		= 'main'
    map			= 'map'
    mark		= 'mark'
    meta		= 'meta'
    meter		= 'meter'
    nav			= 'nav'
    noscript	= 'noscript'
    object		= 'object'
    ol			= 'ol'
    optgroup	= 'optgroup'
    option		= 'option'
    output		= 'output'
    p			= 'p'
    param		= 'param'
    picture		= 'picture'
    pre			= 'pre'
    progress	= 'progress'
    q			= 'q'
    rp			= 'rp'
    rt			= 'rt'
    ruby		= 'ruby'
    s			= 's'
    samp		= 'samp'
    script		= 'script'
    section		= 'section'
    select		= 'select'
    small		= 'small'
    source		= 'source'
    span		= 'span'
    strong		= 'strong'
    style		= 'style'
    sub			= 'sub'
    summary		= 'summary'
    sup			= 'sup'
    svg			= 'svg'
    table		= 'table'
    tbody		= 'tbody'
    td			= 'td'
    template	= 'template'
    textarea	= 'textarea'
    tfoot		= 'tfoot'
    th			= 'th'
    thead		= 'thead'
    time		= 'time'
    title		= 'title'
    tr			= 'tr'
    track		= 'track'
    u			= 'u'
    ul			= 'ul'
    var			= 'var'
    video		= 'video'
    wbr			= 'wbr'



class Framework:
    """ The Framework class is responsible for
    setting the skeleton src variables. """
    def __init__(self):
        """ Initalizing the variables used in
        the end product (HTMLDOC). """
        # Doc Lang
        self._lang = ''
        # HTML Page Title
        self._title = ''
        # Charset (ex. UTF-8)
        self._charset = ''
        # Author, aka. probably YOU!
        self._author = ''
        # CSS File to be linked
        self._css_file = ''
        # Content in <body>
        self._content = ''

    def render(self):
        """ This function will render your product of an file
        it'll contain all the variables you defined in runtime. """
        # Retrieving skeleton from get_skeleton() function
        skeleton = get_skeleton()
        
        # Formatting skeleton, with given variables out of __init__
        skeleton.format(
            lang=self._lang,
            title=self._title, 
            char=self._charset, 
            author=self._author,
            css_file=self._css_file,
            content=self._content
        )

    def add_element(self, tag: Tags, content, **kw):
        """ Method responsible for adding various elements
        to the content in <body> in your HTMLDOC. """
        self._content += f'<{tag}>'


    def lang(self, lang: str):
        """ Function that sets language of
        HTMLDOC. """
        self._lang = lang

    def title(self, title: str):
        """ Function that sets title of
        HTMLDOC. """
        self._title = title

    def charset(self, charset: str):
        """ Function that sets charset of
        HTMLDOC. """
        self._charset = charset

    def author(self, author: str):
        """ Function that sets author of
        HTMLDOC. """
        self._author = author
    
    def link_css(self, link_file: str):
        """ Function that sets the CSS file 
        to be linked to the HTMLDOC. """
        self._css_file = link_file


Frame = Framework()
Frame.render()
