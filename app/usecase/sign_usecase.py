class SignUsecase:
    @staticmethod
    def assign_sign_to_planets(planet_positions: list[float]) -> list[int]:
        return [int(planet_position // 30) for planet_position in planet_positions]
