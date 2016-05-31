# Global voice commands on desktop

# Desktop navigation
Downward                              = { Down_20 };
Upward                                = { Up_20 };

# Basic text navigation
Shup                                  = {Shift+Up};

Shab                                  = {Shift+Tab};

Dunk                                  = {Enter};

E dunk                                = {End} {Enter};
Dunk 2..99                            = {Enter_$1};
Mup                                   = {Up};

Mup 2..99                             = {Up_$1};
Dup                                   = {Down};

Dup 2..99                             = {Down_$1};
Meft                                  = {Left};
Meft 2..99                            = {Left_$1};
Might                                 = {Right};
Might 2..99                           = {Right_$1};
E line                                = {End};

De line                               = {End} {Shift + Home} {Del};
Sline                                 = {End} {Shift + Home};


Bo line                               = {Home};
Seco line                             = {End} ';';
Seco du                               = {End} ';' {Enter};
Reco line                             = {End} ':';
Reco du                               = {End} ':' {Enter};
Cleft                                 = {Ctrl + Left};
Cleft 1..99                           = {Ctrl + Left_$1};
Crait                                 = {Ctrl + Right};
Crait 1..99                           = {Ctrl + Right_$1};
Fithi                                 = {Ctrl + f};
Seep                                  = {Space};
Seep 2..99                            = {Space_$1};

# Killing and yanking and stuff

Kill                                  = {Ctrl+x};

Yank                                  = {Ctrl+v};

Steal                                 = {Ctrl+c};

Crap                                  = {Ctrl+z};

S kill                                = {Home} {Shift+End} {Ctrl+x};

D Kill                                = {Home} {Shift+Down} {Shift+End} {Ctrl+x};

T Kill                                = {Home}{Shift+Down} {Shift+Down} {Shift+End} {Ctrl+x};

Overkill                              = {Home}{Shift+Down} {Shift+Down} {Shift+Down} {Shift+End} {Ctrl+x};

Derr                                  = {Ctrl + Right} {Ctrl + Backspace};
Derr 2..99                            = {Ctrl + Right_$1} {Ctrl + Backspace_$1};
Deft                                  = {Ctrl + Backspace};
Deft 2..99                            = {Ctrl + Backspace_$1};
Sanno                                 = { Ctrl + s };
Bass                                  = {Backspace};
Bass 2..99                            = {Backspace_$1};




# General formatting
Indent                                = {Space_4};
Prain                                 = '()' {Left};
Okra                                  = '{';
Krax                                  = '{}' {Left};
Brax                                  = '[]' {Left};
Obra                                  = '[';
Squotes                               = "''" {Left};
Duotes                                = '""' {Left};

# Math symbols
Leta                                  = {<};
Greta                                 = {>};
Pew                                   = {+};
Pec                                   = '+=';
Spew                                  = {Space} {+} {Space};
Spec                                  = {Space} '+=' {Space};
Nay                                   = {-};
Nayc                                  = '=-';
Snay                                  = {Space} {-} {Space};
Snayc                                 = {Space} '=-' {Space};
Ek                                    = '=';
Sec                                   = {Space} '=' {Space};

# Bash commands
Chadirr                               = {c} {d} {Space};
Ellis                                 = {l} {s} { Space };
Tilde                                 = '~';