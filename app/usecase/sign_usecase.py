class SignUsecase:
    @staticmethod
    def assign_signs_to_planets(planet_positions: list[float]) -> list[int]:
        """
        Assign astrological signs to planet positions.

        Parameters:
        - planet_positions (list[float]): List of planet positions.

        Returns:
        - list[int]: List of assigned astrological signs.
        """
        return [int(planet_position // 30) + 1 for planet_position in planet_positions]
