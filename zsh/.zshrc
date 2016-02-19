# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=20000
SAVEHIST=20000
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/Users/ankitmittal/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall


#copying for autojump utility
[[ -s $(brew --prefix)/etc/profile.d/autojump.sh ]] && . $(brew --prefix)/etc/profile.d/autojump.sh

#setting up aliases
source $HOME/.alias
source $HOME/.func
source /Users/ankitmittal/repos/external/zsh-git-prompt/zshrc.sh
PROMPT='%B%m%~%b$(git_super_status) %# '
#PROMPT='%B%~%b$(git_super_status) %# '
zstyle ':completion:*' '' matcher-list 'm:{a-z}={A-Z}'

hx() {
    var="NR=="
    $(awk $var$1 ~/.histfile)
}

# automatically do an ls after doing cd
chpwd() {
  ls -G
}

PATH=$PATH:/usr/local/sbin

