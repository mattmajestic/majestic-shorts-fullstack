## Docs Route Setup with the following

```bash
npm install @next/mdx @mdx-js/loader @mdx-js/react
```

```
import withMDX from '@next/mdx';

const mdxConfig = withMDX({
  extension: /\.mdx?$/
});

const nextConfig = {
  ...mdxConfig,
  pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
};

export default nextConfig;

```

