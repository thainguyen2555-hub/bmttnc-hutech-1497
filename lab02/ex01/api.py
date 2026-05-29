from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

# PLAYFAIR CIPHER ALGORITHM
playfair_cipher = PlayFairCipher()

from flask import Flask, request, jsonify
from cipher.railfence import RailFenceCipher   # import class RailFenceCipher

app = Flask(__name__)

# Khởi tạo đối tượng RailFenceCipher
railfence_cipher = RailFenceCipher()

# API mã hóa
@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

# API giải mã
@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/api/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']   # FIX

    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)

    return jsonify({'encrypted_text': encrypted_text})


@app.route("/api/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']   # FIX

    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)

    return jsonify({'decrypted_text': decrypted_text})


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])   # giữ nguyên OK vì Caesar dùng số

    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)

    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])   # giữ nguyên OK

    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)

    return jsonify({'decrypted_message': decrypted_text})


@app.route("/api/playfair/matrix", methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)

    return jsonify({'playfair_matrix': playfair_matrix})


@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)

    encrypted_text = playfair_cipher.playfair_encrypt(
        plain_text,
        playfair_matrix
    )

    return jsonify({'encrypted_text': encrypted_text})



@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)

    # FIX: đảm bảo cipher_text luôn chẵn ký tự
    if len(cipher_text) % 2 != 0:
        cipher_text = cipher_text + "X"

    decrypted_text = playfair_cipher.playfair_decrypt(
        cipher_text,
        playfair_matrix
    )

    return jsonify({'decrypted_text': decrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)