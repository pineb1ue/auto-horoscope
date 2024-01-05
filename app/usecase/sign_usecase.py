class SignUsecase:
    @staticmethod
    def assign_signs_to_planets(planet_positions: list[float]) -> list[int]:
        return [int(planet_position // 30) + 1 for planet_position in planet_positions]
