class CoinValidator:
    def __init__(self):
        # Definisikan parameter koin yang valid
        self.valid_coins = {
            'NICKEL': {
                'diameter': 21.21,  # mm
                'weight': 5.0,      # gram
                'thickness': 1.95,  # mm
                'value': 0.05       # USD
            },
            'DIME': {
                'diameter': 17.91,
                'weight': 2.268,
                'thickness': 1.35,
                'value': 0.10
            },
            'QUARTER': {
                'diameter': 24.26,
                'weight': 5.670,
                'thickness': 1.75,
                'value': 0.25
            }
        }
        
        # Toleransi untuk pengukuran (dalam persen)
        self.tolerance = 0.05  # 5% toleransi
        
    def validate_coin(self, coin_params):
        """
        Memvalidasi koin berdasarkan parameter fisiknya
        Returns: (is_valid, coin_type, value) atau (False, None, 0) jika tidak valid
        """
        try:
            for coin_type, specs in self.valid_coins.items():
                # Cek apakah semua parameter dalam toleransi
                diameter_match = self._is_within_tolerance(coin_params['diameter'], 
                                                        specs['diameter'])
                weight_match = self._is_within_tolerance(coin_params['weight'], 
                                                     specs['weight'])
                thickness_match = self._is_within_tolerance(coin_params['thickness'], 
                                                        specs['thickness'])
                
                if diameter_match and weight_match and thickness_match:
                    return True, coin_type, specs['value']
                    
            # Jika tidak ada yang cocok, return sebagai slug
            return False, None, 0
            
        except KeyError:
            # Jika parameter tidak lengkap, anggap sebagai slug
            return False, None, 0
            
    def _is_within_tolerance(self, measured, expected):
        """
        Cek apakah nilai terukur masih dalam batas toleransi
        """
        lower_bound = expected * (1 - self.tolerance)
        upper_bound = expected * (1 + self.tolerance)
        return lower_bound <= measured <= upper_bound

class VendingMachine:
    def __init__(self):
        self.coin_validator = CoinValidator()
        self.payment = 0
        
    def accept_payment(self, coin_params):
        """
        Memproses pembayaran sesuai PSPEC 1.1-1.3
        """
        # PSPEC 1.1: Validate Coins
        is_valid, coin_type, value = self.coin_validator.validate_coin(coin_params)
        
        if is_valid:
            # PSPEC 1.3: Accumulate Payment
            self.payment += value
            return f"Accepted {coin_type}. Current payment: ${self.payment:.2f}"
        else:
            return "Rejected: SLUG"
            
    def clear_payment(self):
        """
        PSPEC 1.2: Clear Payment
        """
        self.payment = 0
        return "Payment cleared"

# Contoh penggunaan
if __name__ == "__main__":
    vm = VendingMachine()
    
    # Contoh koin quarter valid
    quarter = {
        'diameter': 24.26,
        'weight': 5.670,
        'thickness': 1.75
    }
    
    # Contoh slug (koin palsu)
    slug = {
        'diameter': 24.00,
        'weight': 4.500,
        'thickness': 1.50
    }
    
    # Test validasi
    print(vm.accept_payment(quarter))  # Should accept
    print(vm.accept_payment(slug))     # Should reject
    print(f"Total payment: ${vm.payment:.2f}")
    print(vm.clear_payment())