from boilerplate.animated_sprite    import AnimatedSprite
from boilerplate.animation_state    import AnimationState


class MultiAnimatedSprite(AnimatedSprite):
    """
    Animated sprite with multiple animations available depending on state.
    """

    def __init__(self, animation_dict, position):
        self.animation_dict = animation_dict
        self.current_animation_state = AnimationState.IDLE
        start_animation = self.animation_dict[self.current_animation_state]

        self.current_scale = 1
        super().__init__(start_animation, position)

    def change_animation(self, new_animation_state):
        """
        Change the sprite's state and it's current animation.
        """
        if self.current_animation_state != new_animation_state:
            self.current_animation_state = new_animation_state
            new_animation = self.animation_dict.get(new_animation_state, 
                                        self.animation_dict[AnimationState.IDLE])
            self.reset(new_animation, self.rect.topleft)
            self.scale_animation(1)

    def scale_animation(self, scale_factor):
        self.current_scale *= scale_factor
        scaled_animations = (self.animation_dict[self.current_animation_state]
                                .scale(self.current_scale))
        self.images = scaled_animations
        self.rect = self.images[0].get_rect()
