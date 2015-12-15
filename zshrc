# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=10000
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
source /Users/ankitmittal/repos/external/zsh-git-prompt/zshrc.sh
#PROMPT='%B%m%~%b$(git_super_status) %# '
PROMPT='%B%~%b$(git_super_status) %# '
zstyle ':completion:*' '' matcher-list 'm:{a-z}={A-Z}'

cd () {
  builtin cd "$@" 2>/dev/null && return
  emulate zsh
  setopt local_options extended_glob
  local matches
  matches=( (#i)${(P)#}(N/) )
  case $#matches in
    0) # There is no match, even case-insensitively. Try cdpath.
      if ((#cdpath)) &&
         [[ ${(P)#} != (|.|..)/* ]] &&
         matches=( $^cdpath/(#i)${(P)#}(N/) ) &&
         ((#matches==1))
      then
        builtin cd $@[1,-2] $matches[1]
        return
      fi
      # Still nothing. Let cd display the error message.
      builtin cd "$@";;
    1)
      builtin cd $@[1,-2] $matches[1];;
    *)
      print -lr -- "Ambiguous case-insensitive directory match:" $matches >&2
      return 3;;
  esac
}

hx() {
    var="NR=="
    $(awk $var$1 ~/.histfile)
}
