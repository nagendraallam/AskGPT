pkgname=terminal-chatgpt
pkgver=0.0.1
pkgdesc="A terminal chat application using GPT-4 to help you become pro at linux"
arch=('any')
url="https://github.com/nagendraallam/terminal-chatgpt"
license=('MIT')

build() {

}

package() {
    # install dependencies and main.py script
    pip install -r requirements.txt
    mkdir -p "$pkgdir/usr/bin/chatbot"
    chmod +x main.py
    mv main.py "$pkgdir/usr/bin/chatbot/"
    mv chatbot.py "$pkgdir/usr/bin/chatbot/"
    mv .env "$pkgdir/usr/bin/chatbot/"
}
