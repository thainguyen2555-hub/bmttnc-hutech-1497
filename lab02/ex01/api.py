from flask import Flask, request, jsonify
from flask_cors import CORS

# Import các cipher
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)
CORS(app)  # Cho phép client gọi API từ domain khác

# Khởi tạo các cipher
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
playfair_cipher = PlayFairCipher()
railfence_cipher = RailFenceCipher()


# ==================== CAESAR CIPHER ====================
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.json
        plain_text = data.get('plain_text', '')
        key = int(data.get('key', 0))
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = request.json
        cipher_text = data.get('cipher_text', '')
        key = int(data.get('key', 0))
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ==================== VIGENERE CIPHER ====================
@app.route("/api/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    try:
        data = request.json
        plain_text = data.get('plain_text', '')
        key = data.get('key', '')
        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route("/api/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    try:
        data = request.json
        cipher_text = data.get('cipher_text', '')
        key = data.get('key', '')
        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ==================== PLAYFAIR CIPHER ====================
@app.route("/api/playfair/matrix", methods=['POST'])
def playfair_creatematrix():
    try:
        data = request.json
        key = data.get('key', '')
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        return jsonify({'playfair_matrix': playfair_matrix})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    try:
        data = request.json
        plain_text = data.get('plain_text', '')
        key = data.get('key', '')
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    try:
        data = request.json
        cipher_text = data.get('cipher_text', '')
        key = data.get('key', '')
        
        # Đảm bảo cipher_text luôn chẵn ký tự
        if len(cipher_text) % 2 != 0:
            cipher_text = cipher_text + "X"
        
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ==================== RAIL FENCE CIPHER ====================
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        data = request.json
        plain_text = data.get('plain_text', '')
        key = int(data.get('key', 2))
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    try:
        data = request.json
        cipher_text = data.get('cipher_text', '')
        key = int(data.get('key', 2))
        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ==================== TEST ENDPOINT ====================
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'API Server is running!',
        'status': 'ok',
        'endpoints': [
            'POST /api/caesar/encrypt',
            'POST /api/caesar/decrypt',
            'POST /api/vigenere/encrypt',
            'POST /api/vigenere/decrypt',
            'POST /api/playfair/encrypt',
            'POST /api/playfair/decrypt',
            'POST /api/playfair/matrix',
            'POST /api/railfence/encrypt',
            'POST /api/railfence/decrypt'
        ]
    })


if __name__ == "__main__":
    print("Starting API Server...")
    print("Server running at: http://127.0.0.1:5000")
    print("Available endpoints:")
    print("  POST /api/caesar/encrypt")
    print("  POST /api/caesar/decrypt")
    print("  POST /api/vigenere/encrypt")
    print("  POST /api/vigenere/decrypt")
    print("  POST /api/playfair/encrypt")
    print("  POST /api/playfair/decrypt")
    print("  POST /api/playfair/matrix")
    print("  POST /api/railfence/encrypt")
    print("  POST /api/railfence/decrypt")
    app.run(host="0.0.0.0", port=5000, debug=True)