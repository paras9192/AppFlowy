import { useLocation } from 'react-router-dom';
import { useMemo } from 'react';

export function useMoreOptionsConfig() {
  const location = useLocation();

  const { type, pageType, id } = useMemo(() => {
    const [_, type, pageType, id] = location.pathname.split('/');

    return {
      type,
      pageType,
      id,
    };
  }, [location.pathname]);

  const showMoreButton = useMemo(() => {
    return type === 'page';
  }, [type]);

  const showStyleOptions = useMemo(() => {
    return type === 'page' && pageType === 'document';
  }, [pageType, type]);

  return {
    showMoreButton,
    showStyleOptions,
  };
}
