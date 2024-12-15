# Contributing to Kairos

## Development Process

1. **Fork & Clone**
   - Fork the repository on GitHub
   - Clone your fork locally
   ```bash
   git clone git@github.com:username/kairos.git
   ```

2. **Set Up Development Environment**
   - Install GHC and Cabal
   - Install development tools:
     ```bash
     cabal update
     cabal install hlint
     cabal install haddock
     ```

3. **Create a Branch**
   - Create a branch for your feature/fix
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Development Guidelines**

   ### Framework Authority
   - Always prioritize official framework/library documentation
   - Document any deviations from framework recommendations
   - Resolve and document conflicts between frameworks

   ### Code Style
   - Follow Haskell Style Guide
   - Use meaningful variable names
   - Document complex logic
   - Add type signatures to all top-level bindings

   ### Testing
   - Write tests for new functionality
   - Ensure all tests pass locally
   - Add property-based tests where appropriate

   ### Documentation
   - Update documentation for new features
   - Add Haddock comments to exported functions
   - Include examples in documentation

5. **Commit Guidelines**
   - Write clear commit messages
   - Reference issues in commits
   - Keep commits focused and atomic

6. **Pull Request Process**
   - Update documentation
   - Add tests
   - Ensure CI passes
   - Fill out PR template completely
   - Request review from maintainers

## Project Structure

```
kairos/
├── src/                    # Source code
│   ├── Kairos/
│   │   ├── Core/          # Core types and functionality
│   │   ├── Pattern/       # Pattern system
│   │   ├── MCP/          # Model Context Protocol
│   │   └── Proof/        # Proof system
├── test/                   # Test suite
├── docs/                   # Documentation
└── scripts/                # Development scripts
```

## Development Workflow

1. **Issue First**
   - Start with an issue
   - Get agreement on approach
   - Reference issue in PR

2. **Branch Strategy**
   - `main` is protected
   - Feature branches from `main`
   - PRs merge back to `main`

3. **Review Process**
   - CI must pass
   - Code review required
   - Documentation updated
   - Tests included

## Getting Help

- Open an issue for questions
- Join project discussions
- Read the documentation

## License

By contributing, you agree that your contributions will be licensed under the project's MIT license.
