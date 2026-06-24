import pygame

from codigo.Player import Player
from codigo.Enemy import Enemy
from codigo.PlayerShot import PlayerShot
from codigo.EnemyShot import EnemyShot

class EntityMediator:
    @staticmethod
    def verify_collisions(entity_list):
        score_gained = 0
        player = None
        for entity in entity_list:
            if isinstance(entity, Player):
                player = entity
                break
        if player is None:
            return 0
        entities_to_remove = []

        for entity in entity_list:
            if not isinstance(entity, PlayerShot):
                continue
            for target in entity_list:
                if not isinstance(target, Enemy):
                    continue
                
                if entity.rect.colliderect(target.rect):
                    target.health -= 1
                    
                    if entity not in entities_to_remove:
                        entities_to_remove.append(entity)

                    if target.health <= 0:
                        player.score += target.score
                        score_gained += target.score

                        if target not in entities_to_remove:
                            entities_to_remove.append(target)

        for entity in entity_list:
            if not isinstance(entity, EnemyShot):
                continue
            
            if entity.rect.colliderect(player.rect):
                player.health -= 1
                
                if entity not in entities_to_remove:
                    entities_to_remove.append(entity)

        for entity in entities_to_remove:
            if entity in entity_list:
                entity_list.remove(entity)

        return score_gained

    @staticmethod
    def remove_offscreen(entity_list):
        entities_to_remove = []
        for entity in entity_list:
            if isinstance(entity, PlayerShot):
                if entity.rect.bottom < 0:
                    entities_to_remove.append(entity)
 
            elif isinstance(entity, EnemyShot):
                if entity.rect.top > 768:
                    entities_to_remove.append(entity)

        for entity in entities_to_remove:
            if entity in entity_list:
                entity_list.remove(entity)

    @staticmethod
    def player_alive(entity_list):

        for entity in entity_list:
            if isinstance(entity, Player):
                return entity.health > 0

        return False

    @staticmethod
    def enemies_remaining(entity_list):
        total = 0

        for entity in entity_list:
            if isinstance(entity, Enemy):
                total += 1

        return total