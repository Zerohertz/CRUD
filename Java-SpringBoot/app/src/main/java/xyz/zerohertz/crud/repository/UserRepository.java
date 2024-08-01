package xyz.zerohertz.crud.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import xyz.zerohertz.crud.model.User;

public interface UserRepository extends JpaRepository<User, Long> {
}
