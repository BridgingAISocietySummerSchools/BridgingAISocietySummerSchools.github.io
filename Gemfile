source "https://rubygems.org"

# Monkeypatch for Ruby 3.2+ compatibility (Jekyll 3.x/Liquid 4.x)
if RUBY_VERSION >= "3.2"
  [Object, String, Array, Hash].each do |klass|
    klass.class_eval do
      def tainted?; false; end
      def taint; self; end
      def untaint; self; end
      def untrusted?; false; end
      def trust; self; end
      def untrust; self; end
    end
  end
end

gem "github-pages", group: :jekyll_plugins
gem "jekyll-include-cache", group: :jekyll_plugins
gem "csv"
gem "bigdecimal"
gem "webrick"

