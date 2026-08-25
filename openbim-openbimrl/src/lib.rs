//! Reserved OpenBIM.rs namespace for the `openbim-openbimrl` package.
//!
//! No parser, language implementation, validation behavior, or standards-body
//! affiliation is provided or implied.

#![forbid(unsafe_code)]

/// The package's deliberately limited status.
pub const PACKAGE_STATUS: &str =
    "RESERVED OpenBIM.rs namespace; no authoritative specification or implementation is provided.";

#[cfg(test)]
mod tests {
    use super::PACKAGE_STATUS;

    #[test]
    fn status_is_explicitly_reserved() {
        assert!(PACKAGE_STATUS.starts_with("RESERVED "));
    }
}
